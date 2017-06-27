# using markovify, generates very nice output.
# very nice output
import markovify

# Get raw text as string.
with open("../output/my-messages-only/xFF5353.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

'''
# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

print()
'''

# Print three randomly-generated sentences of no more than 140 characters
print( text_model.make_short_sentence(140) )
# for i in range(3):
#     print(text_model.make_short_sentence(140))

