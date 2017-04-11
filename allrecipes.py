import requests
import sys
import random
from twilio.rest import TwilioRestClient

client = TwilioRestClient("AC845a2929747421859952fe310c2f7fc1", "456bb393c12b0f6d5209403d97812ea7")
searchUrl = 'http://food2fork.com/api/search'
getUrl = 'http://food2fork.com/api/get'
key = 'b4e3f32f9f51ebe397a80d531ef6cc35'
if len(sys.argv) < 2:
	print'Need extra argument'
else:
	count = 1
	q = ''
	filename = ''
	while count < len(sys.argv):
		filename += sys.argv[count]
		q += sys.argv[count] + ' '
		count += 1
	filename += '.txt'
	f = open(filename, 'w')
	params = [('key', key), ('q', q)]
	r = requests.get(searchUrl, params=params)
	temp = r.json()['recipes']
	randNum = random.randint(0, len(temp) - 1)
	sentRecipe = ''
	count = 0

	for x in temp:
		if count == randNum:
			sentRecipe += x['title'] + ':\n'
		title = x['title'] + ':\n'
		title = title.encode('utf-8')
		f.write(title)
		recipeID = x['f2f_url'][26:]
		params = [('key', key), ('rId', recipeID)]
		r = requests.get(getUrl, params=params)
		ingredients = r.json()['recipe']['ingredients']
		for y in ingredients:
			if count == randNum:
				sentRecipe += y + '\n'
			f.write(y)
			f.write('\n')
		f.write('\n')
		count += 1
	f.close()
	print sentRecipe
	client.messages.create(to="+12138148304", from_="+13106834831", 
                       body=sentRecipe)

#using a websites api
#using command lines argv
#writing to a file
#using twilio to send messages

#python allrecipes.py [ingredient]
