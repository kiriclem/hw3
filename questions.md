QUESTIONS:

1. how and where do I use function arguments in the assignment?

2. should there be a 'for' loop in the 'apply templates' function?

3. I want the 'apply templates' function to accept a specific page as an argument, how do I do that? for example, if I wanted to only apply the template to the 'about me' page: 

	def apply_template(page):
		template = open('templates/base.html').read()
		page_content = **open the page specified as the argument**.read()
		fin_page = template.replace('{{content}}', page_content)
		return fin_page 
		
	apply_template('about me')
