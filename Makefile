serve:
	bundle exec jekyll serve --livereload

check-links:
	bundle exec jekyll build
	bundle exec htmlproofer ./_site
