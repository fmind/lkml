OUTPUT="mails.json"
FORMAT="jsonlines"
LOGLEVEL="INFO"

all:
	rm -f $(OUTPUT)
	scrapy crawl mails -o $(OUTPUT) -t $(FORMAT) -L $(LOGLEVEL)
