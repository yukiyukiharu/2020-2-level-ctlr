### Stage 1. Retrieve raw data from World Wide Web

> Python competencies required:
> * working with external dependencies, going beyond Python standard library
> * working with modules as parametrized applications (CLI - command line interface)
> * working with files: create/read/update
> * downloading web pages
> * parsing web pages as HTML structure

Downloader application should work according to the given interface of the config file.

|CLI argument|Description|Example|
|:---|:---|:---|
|`--base-url`|URL of the newspaper that contains the list of items to retrieve|`https://www.nn.ru/text/?page=2`|
|`--num-articles`|Number of articles to download|`100`|

Example execution:

```bash
py scrapper.py --base-url https://www.nn.ru/text/?page=2 --num-articles 100
```

Expected result:
1. 100 articles from the given URL are parsed
1. all articles are downloaded to the `tmp` directory. `tmp` directory content:
```
+-- 2020-2-level-ctlr
    +-- tmp
        +-- articles
            +-- 1_raw.txt <- the paper with the ID as the name
            +-- 1_meta.json <- the paper meta-information
            +-- ...
```

> NOTE: When using CI (Continuous Integration), generated `dataset.zip` is available in
> build artifacts. Instructions on obtaining build artifacts *TBD*.
