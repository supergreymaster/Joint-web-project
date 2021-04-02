rgb = "255 128 64"

# text = '#' + ''.join([f"{int(i):02x}" for i in rgb.split(',')])
# text = '#' + ''.join(map(lambda i: f"{int(i):02x}", rgb.split()))
text = '#' + ''.join(map(lambda i: f"{hex(int(i))}"[2:], rgb.split()))

print(text)