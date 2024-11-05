# Skype database processor
# by Francesco Montorsi, (c) 1-29-2011
#

# constants
# ------------------------------------------------------------------------------
toprocessfn = ['skype_db_backup.db','skype_db_backup_forstWIN.db','skype_db_backup_fioreWIN.db']
outputfn = 'skype_log.html'
sender1 = 'fiorenzabaru'
sender2 = 'f.montorsi'
max_messages = -1      # or -1 to disable!
replacements = {}
replacements['<ss type="angel">(angel)</ss>'] = '<img src=\'skype_icons/skype_angel.png\'/>'
replacements['<ss type="flower">(F)</ss>'] = '<img src=\'skype_icons/skype_flower.png\'/>'
replacements['<ss type="giggle">(chuckle)</ss>'] = '<img src=\'skype_icons/skype_giggle.gif\'/>'
replacements['<ss type="heart">(h)</ss>'] = '<img src=\'skype_icons/skype_heart.gif\'/>'
replacements['<ss type="inlove">(inlove)</ss>'] = '<img src=\'skype_icons/skype_inlove.gif\'/>'
replacements['<ss type="hug">(hug)</ss>'] = '<img src=\'skype_icons/skype_hug.gif\'/>'
replacements['<ss type="kiss">:*</ss>'] = '<img src=\'skype_icons/skype_kiss.png\'/>'
replacements['<ss type="kiss">:-*</ss>'] = '<img src=\'skype_icons/skype_kiss.png\'/>'
replacements['<ss type="smile">:)</ss>'] = '<img src=\'skype_icons/skype_smile.png\'/>'
replacements['<ss type="smile">:-)</ss>'] = '<img src=\'skype_icons/skype_smile.png\'/>'
replacements['<ss type="yes">(y)</ss>'] = '<img src=\'skype_icons/skype_yes.png\'/>'
replacements['<ss type="laugh">:D</ss>'] = '<img src=\'skype_icons/skype_laugh.png\'/>'
replacements['<ss type="laugh">:-D</ss>'] = '<img src=\'skype_icons/skype_laugh.png\'/>'
replacements['<ss type="wink">;)</ss>'] = '<img src=\'skype_icons/skype_wink.png\'/>'
replacements['<ss type="wink">;-)</ss>'] = '<img src=\'skype_icons/skype_wink.png\'/>'
replacements['<ss type="rofl">(rofl)</ss>'] = '<img src=\'skype_icons/skype_rofl.gif\'/>'
replacements['<ss type="hi">(wave)</ss>'] = '<img src=\'skype_icons/skype_wave.gif\'/>'
replacements[sender1] = 'Fiore'
replacements[sender2] = 'Fra'
colours = {}
colours[sender1] = 'red'
colours[sender2] = 'green'
max_minutes_per_session = 60*4

# modules
# ------------------------------------------------------------------------------
import fileinput
import sqlite3
from datetime import datetime

# classes
# ------------------------------------------------------------------------------
class ChatEntry:
    def __init__(self, datetime, sender, msg, chatid):
        self.datetime = datetime
        self.sender = sender
        self.msg = msg
        self.chatid = chatid
                # used when loading all messages at the beginning from Sqlite DB

    def __lt__(self, other):
        return self.datetime < other.datetime
    def compareForDuplicates(self, other):
        timediff = self.datetime-other.datetime
        secdifference = timediff.days*1440*60 + timediff.seconds
        return self.sender == other.sender and self.msg == other.msg and secdifference <= 1
    
class ChatSession:
    def __init__(self, chatid, start_datetime):
        self.chatid = chatid
        self.start_datetime = start_datetime
        self.end_datetime = None
        self.entries = []
        
    def length(self):       # in minutes
        l = self.end_datetime - self.start_datetime
        return int(l.days*1440 + l.seconds/60)

    def __lt__(self, other):
        return self.start_datetime < other.start_datetime


# utility functions
# ------------------------------------------------------------------------------

def findDuplicated(entry,db):
    for e in db:
        if e.compareForDuplicates(entry):
            return e
    return None
def buildp(content, sender):
    return '<p style=\'color:' + colours[sender] + '\'>' + content+ '</p>'
def buildspan(content, sender):
    return '<span style=\'color:' + colours[sender] + '\'>' + content+ '</span>'
def buildchattitle(session, compact=0):
    minutes = session.length()
    hours = int(minutes/60)
    if compact:
        ret = session.start_datetime.strftime('Day %d at %H:%M ')
    else:
        ret = session.start_datetime.strftime('Chat of %d %B %Y at %H:%M ')
    if minutes < 60:
        return ret + '(length: %d min)' % minutes
    else:
        return ret + '(length: %d hour(s) and %d min)' % (hours, minutes - hours*60) 
    

# SCRIPT MAIN
# ------------------------------------------------------------------------------

# get list of interesting conversations
db = []
total = 0
for filefn in toprocessfn:
    print(('Processing file: %s' % filefn))
    conn = sqlite3.connect(filefn)
    cursor = conn.cursor()
    cursor.execute('select timestamp,author,body_xml,chatname from Messages where type=61 and author=\'' + sender1 + '\' or author=\'' + sender2 + '\' order by timestamp')
    partial = 0
    duplicated = 0
    for lst in cursor:
        partial = partial + 1
        dt = datetime.fromtimestamp(lst[0])
        sender = lst[1]
        msg = lst[2]
        chatid = lst[3]
        if msg != None and sender1 in chatid and sender2 in chatid:
            # ok, this message needs to be processed
            entry = ChatEntry(dt,sender,msg,chatid)
            idxDup = findDuplicated(entry,db)
            if idxDup == None:
                db.append(entry)
                #print('  ',sender,msg)
                #print('    ', dt, chatid)
                if max_messages != -1 and len(db) > max_messages: break
            else:
                duplicated = duplicated + 1
#                print('  ...found duplicated:\n\tmsg1: [%s] %s\n\tmsg2: [%s] %s'
#                      % (dt.strftime('%d/%M/%Y %H:%M'), msg, entry.datetime.strftime('%d/%M/%Y %H:%M'), entry.msg))
    print((' ...found %d entries (%d duplicated!)' % (partial,duplicated)))
    total = total + partial
    cursor.close()
    conn.close()

print(('Loaded %d/%d chat messages' % (len(db),total)))

# split chat sessions which are too long in time!
# (NOTE: we assume all chat entries are ordered by datetime!)
sessions = []
cs = ChatSession(db[0].chatid, db[0].datetime)      # create the first session
cs.entries.append(db[0])
sessions.append(cs)
previous_chatid = db[0].chatid
for idx in range(1,len(db)):
    entry = db[idx]
    current_chatid = entry.chatid
    if current_chatid == previous_chatid:
        # update last session's end time
        sessions[-1].end_datetime = entry.datetime
        
        # seems to belong to the same chat session... look at the time!!        
        if sessions[-1].length() > max_minutes_per_session:
            # close current session with last chat message
            sessions[-1].end_datetime = db[idx-1].datetime
            #print('last session had %d messages' % len(sessions[-1].entries))
            
            # create new session
            current_chatid = current_chatid + 's'
            sessions.append(ChatSession(current_chatid, entry.datetime))
            #print('new session at', entry.datetime)

            # update all following messages' chatid of our 'database' to the new chatid
            for idx2 in range(idx,len(db)):
                if db[idx2].chatid == previous_chatid:
                    db[idx2].chatid = current_chatid

            assert(db[idx].chatid == current_chatid)
            sessions[-1].entries.append(db[idx])

            previous_chatid = current_chatid
        else:
            # just append this message to the last session...
            sessions[-1].entries.append(entry)

    else:
        # insert new chat session 
        sessions.append(ChatSession(entry.chatid, entry.datetime))

        assert(entry.chatid == current_chatid)
        sessions[-1].entries.append(entry)
        #print('new session at', entry.datetime)
        previous_chatid = entry.chatid

    #print(db[idx].datetime,db[idx].chatid)

sessions[-1].end_datetime = db[-1].datetime   # update last session end time!
print(('Detected %d chat sessions' % len(sessions)))

# security check
totalcount = 0
for session in sessions:
    totalcount = totalcount + len(session.entries)
assert(totalcount == len(db))       # make sure no messages have been lost!
del db

# merge consecutive messages of the same sender in the same chat session
for session in sessions:
    newentries = []

    # process all entries for this session
    entry1idx = 0
    while entry1idx < len(session.entries):
        #print('now at ', entry1idx, ':', session.entries[entry1idx].msg)
        for entry2idx in range(entry1idx+1,len(session.entries)-1):
            if session.entries[entry1idx].sender != session.entries[entry2idx].sender:
                break
            #print('  ', entries[entry1idx].sender, entries[entry2idx].sender)

        # merge consecutive entries of the same sender
        #print('merging from ', entry1idx, ' to ', entry2idx)
        newEntry = session.entries[entry1idx]
        for entry in session.entries[entry1idx+1:entry2idx]:
            assert(entry.sender == session.entries[entry1idx].sender)
            assert(entry.chatid == session.chatid)#entries[entry1idx].chatid)
            newEntry.msg = newEntry.msg + '<br/>' + entry.msg

        #print('new merged entry: ', newEntry.msg)
        newentries.append(newEntry)
        entry1idx = max(entry1idx+1,entry2idx)

    # update the entries for this session
    session.entries = newentries

# format in a nice HTML
print(('Writing to file', outputfn))
out_file = open(outputfn, "w")
out_file.write('<h1>Log of the chats between ' + buildspan(replacements[sender1], sender1) +
                ' and ' + buildspan(replacements[sender2], sender2) + '</h1>')

# divide by month
sorted_sessions = sessions
sorted_sessions.sort()
months = [ [sorted_sessions[0]] ]
for session in sorted_sessions[1:]:
    if session.start_datetime.month == months[-1][0].start_datetime.month:
        months[-1].append(session)
    else:
        months.append([session])

total_length = 0
for month in months:
    out_file.write(month[0].start_datetime.strftime('<h2>%B %Y</h2>'))
    out_file.write('<ul>')
    for session in month:
        out_file.write('<li><a href=\'' + session.chatid + '\'>' + buildchattitle(session,1) + '</a></li>')
        total_length = total_length + session.length()
    out_file.write('</ul>')

out_file.write('<h1>Statistics</h1>')
out_file.write('Number of chats: %d      Length: %d hours' % (len(sorted_sessions), int(total_length/60)))
               
for session in sorted_sessions:
    out_file.write('<h2 id=\'' + session.chatid[1:] + '\'>' +
                   buildchattitle(session) +
                   '</h2>')
    out_file.write(session.start_datetime.strftime('[%d %B %Y - %H:%M]'))
    out_file.write('<table>')
    for entry in session.entries:
        # filter text
        msg = entry.msg
        for torep in list(replacements.keys()):
            msg = msg.replace(torep, replacements[torep])

        # write this message
        out_file.write('<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;</td>' +
                       '<td valign=\'top\'>' + buildp(replacements[entry.sender], entry.sender) + '</td><td>' +
                       buildp(msg, entry.sender) + '</td></tr>')
        
    out_file.write('</table>')
    out_file.write(session.end_datetime.strftime('[%d %B %Y - %H:%M]'))
    
out_file.write('</table>')
out_file.close()
