INFO := simple commit

test:
	@jekyll server

commit:
	@make clean
	@git add .
	@git commit -m "$(INFO)"

push:
	@git push origin main

java-test:
	@javac scripts/PostInfo.java
	@java scripts.PostInfo

update:
	@git pull origin main

.PHONY:
clean:
	@-rm -rf _site