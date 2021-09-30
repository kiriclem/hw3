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

def apply_template(content):
	template = open('templates/base.html').read()
	result = template.replace('{{content}}', content)
	return result

def apply_title(title):	
	template = open('templates/base.html').read()
	result = template.replace('{{title}}', title)
	return result				
	
def main():
	for page in pages:
		content = open(page['filename']).read()
		title = page['title']
		fin_page = apply_template(content)
#		fin_page = apply_title(title)
		open(page['output'], 'w+').write(fin_page)

main()

