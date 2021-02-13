## Dataset requirements

1. Structure:
```
+-- 2020-2-level-ctlr
    +-- tmp
        +-- articles
        +-- raw_dataset.zip
            +-- articles
                +-- 1_raw.txt <- the paper with the ID as the name
                +-- 1_processed.txt <- the tokenized, lemmatized, tagged paper text 
                +-- 1_meta.json <- the paper meta-information
                    {
                        "id": "1",
                        "title": "Власти продлили «дачную амнистию». Разбираемся в нововведениях с NN.RU",
                        "title_xpath": "body > class-14 > .header",
                        "date": "2021-01-26 07:30:00",
                        "url": "https://www.nn.ru/text/realty/2021/01/26/69724161/",
                        "topics": ["недвижимость"], <- Optional. 4 module -> skip-topics=True
                        "author": "Егор Герасимов" <- Optional. .skips -> skip-author=True
                    }
                +-- 2_raw.txt
                +-- 2_processed.txt
                +-- 2_meta.json
                +-- ...
                +-- 100_raw.txt
                +-- 100_processed.txt
                +-- 100_meta.json
```
1. Volume: not less than 100 texts
1. Tagged: each token has inplace tag with morphological information:
   1. *TBD*
1. Recoverability of information (meta-information):
   1. Article name
   1. Article date
   1. Article URL 
   1. Article topics
   1. Article author