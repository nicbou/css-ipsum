#!/usr/bin/env python

# Builds a CSS file for the given lorem ipsum text

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas volutpat imperdiet sollicitudin. Aliquam sed quam urna. Nullam id ipsum eu tellus laoreet volutpat a a mi. Vestibulum varius leo libero, et tristique nulla convallis a. Nulla ultricies magna ac felis euismod bibendum. Nulla justo neque, luctus quis placerat vel, mollis a ante. Aliquam tincidunt risus ante, nec dignissim mi vestibulum non. Pellentesque suscipit luctus metus, in imperdiet augue tincidunt id. Quisque malesuada et nulla non placerat. Duis rutrum lacus at ullamcorper dignissim. Nam eget orci bibendum, ullamcorper risus id, interdum nibh. Nulla rutrum nisi nec enim pellentesque bibendum. Etiam interdum turpis at eros congue tristique. Vivamus mi nisl, dictum in faucibus non, viverra non leo. Ut rutrum ultricies tortor, in volutpat nisl fringilla nec. Praesent ac urna leo. Quisque vel pharetra lectus. Duis blandit nisi sit amet orci mattis, vel hendrerit nunc mollis. Mauris vel lacinia mi. Nulla facilisi. Vivamus.'
element = ''  #Defaults to all elements
attribute = 'data-ipsum'

word_count = 1
sentence = ''
output = '%s[%s]:after{content:"%s"}' % (element, attribute, lorem_ipsum)
for word in lorem_ipsum.split(' '):
    sentence = '%s %s' % (sentence, word)
    output += '\r\n%s[%s="%i"]:after{content:"%s"}' % (element, attribute, word_count, sentence)
    word_count += 1

output_file = open('cssipsum.css', 'w')
output_file.write(output)
output_file.close()
