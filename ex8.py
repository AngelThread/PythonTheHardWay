formatter = "%s %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

print formatter % ( 
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)

# Python prints the strings in the most efficient way it can, not replicate
# exactly way the way they are written. This is perfectly fine since %r is used 
# for debugging and inspection, so it's not neccesary that it be pretty.
