define wchar_print
        echo "

        set $i = 0
        while (1 == 1)
                set $c = (char)(($arg0)[$i++])
                if ($c == '\0')
                        loop_break
                end
                printf "%c", $c
        end

        echo "\n
end

document wchar_print
wchar_print <wstr>
Print ASCII part of <wstr>, which is a wide character string of type wchar_t*.
end

