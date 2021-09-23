def main():
	
	pages = [
		{
			"filename": "content/index.html",
			"output": "docs/index.html",
			"title": "Home",	
		},	
		
		{
			"filename": "content/about.html",
			"output": "docs/about.html",
			"title": "About Me",	
		},
		
		{
			"filename": "content/blog.html",
			"output": "docs/blog.html",
			"title": "Blog",	
		},
		
		{
			"filename": "content/projects.html",
			"output": "docs/projects.html",
			"title": "Projects",	
		}

	]

	templates = {
		"top": "templates/top.html",
		"bottom": "templates/bottom.html",
		}


	for page in pages:
		top = open(templates['top']).read()		
		file_name = open(page['filename']).read()
		bottom = open(templates['bottom']).read()
		full_page = top + file_name + bottom
		open(page['output'], 'w+').write(full_page)


main()
