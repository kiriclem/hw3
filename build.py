# list of pages for website

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

# opens the template page and replaces the content for each page

def apply_template(content, title):
	template = open('templates/base.html').read()
	result = template.replace('{{content}}', content)
	new_result = apply_title(result, title)
	return new_result

# replaces the title so that the browswer displays the correct title for each page 
def apply_title(result, title):	
	result = result.replace('{{title}}', title)
	return result				

# loops through each entry in pages list, saves output 

def main():
	for page in pages:
		content = open(page['filename']).read()
		title = page['title']
		fin_page = apply_template(content, title)
		open(page['output'], 'w+').write(fin_page)

main()

