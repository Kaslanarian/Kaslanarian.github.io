INFO := simple commit

test:
	@jekyll server

commit:
	@make clean
	@git add .
	@git commit -m "$(INFO)"

push:
	@git push origin main

.PHONY:
clean:
	@-rm -rf _site