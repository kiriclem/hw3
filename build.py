def main():
	
	top = open('./templates/top.html').read()
	content = open('./content/index.html').read()
	bottom = open('./templates/bottom.html').read()
	full_site = top + content + bottom
	open('./docs/index.html', 'w+').write(full_site)

	top = open('./templates/top.html').read()
	content = open('./content/blog.html').read()
	bottom = open('./templates/bottom.html').read()
	full_site = top + content + bottom
	open('./docs/blog.html', 'w+').write(full_site)

	top = open('./templates/top.html').read()
	content = open('./content/about.html').read()
	bottom = open('./templates/bottom.html').read()
	full_site = top + content + bottom
	open('./docs/about.html', 'w+').write(full_site)

	top = open('./templates/top.html').read()
	content = open('./content/projects.html').read()
	bottom = open('./templates/bottom.html').read()
	full_site = top + content + bottom
	open('./docs/projects.html', 'w+').write(full_site)
	
pages = [
	{
		"filename": "content/index.html",
		"output": "docs/index.html",
		"title": "Home",	
	}	
	{
		"filename": "content/about.html",
		"output": "docs/about.html",
		"title": "About Me",	
	}
	{
		"filename": "content/blog.html",
		"output": "docs/blog.html",
		"title": "Blog",	
	}
	{
		"filename": "content/projects.html",
		"output": "docs/projects.html",
		"title": "Projects",	
	}

]


main()
