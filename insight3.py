import re, datetime

infile = 'tweets.txt'
tformat = "%a %b %d %H:%M:%S +0000 %Y"

mylist = []
with open(infile, 'r') as fr:
    # New tweet arrives
    for line in fr:
        if "(timestamp: " in line:
            # Split tweet into message and timestamp
            message, timestamp = line.lower().split("(timestamp: ")
            
            # Clean up timestamp
            timestamp = timestamp.replace(")", '').replace("\n", '')
            
            # Convert timestamp string to datetime time
            try:
                tnow = datetime.datetime.strptime(timestamp, tformat)
            except ValueError:
                break
            
            # Extract hashtags, if any, from message
            hashtags  = re.findall(r"#(\w+)", message)
            
            mylist.append((tnow, set(hashtags)))