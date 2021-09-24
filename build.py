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

def apply_template():
	for page in pages:
		template = open('templates/base.html').read()
		page_content = open(page['filename']).read()
		fin_page = template.replace('{{content}}', page_content)
		return fin_page
		
def main():
	for page in pages:
		fin_page = apply_template()
		open(page['output'], 'w+').write(fin_page)

main()

