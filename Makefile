INFO := simple commit

test:
	@make clean
	@jekyll server

commit:
	@make clean
	@git add .
	@git commit -m "$(INFO)"

push:
	@git push origin main

update:
	@git pull origin main

.PHONY:
clean:
	@jekyll clean