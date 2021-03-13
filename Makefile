INFO := simple commit

test:
	@jekyll server

push:
	make clean
	git add .
	git commit -m "$(INFO)"
	git push origin main

.PHONY:
clean:
	@-rm -rf _site