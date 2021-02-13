### Stage 2. Process raw data

Data Processing Pipeline (`pipeline.py`) component should:
1. receive a `paper` folder created by `scrapper.py` as an input
1. tokenize each text
1. lemmatize each text
1. perform morphological analysis of each word in each text
1. tag each word in each text
1. produce a `{\d}_processed.txt` for each `{\d}_raw` article.

Data Processing Pipeline application should work according to the given interface:

|CLI argument|Description|Example|
|:---|:---|:---|
|`--raw-data-directory`|Path to the folder|`./tmp/articles`|

Example execution:

```bash
py pipeline.py --raw-data-directory ./tmp/articles
```

Expected result:
1. each paper has a processed version in `tmp` directory. `tmp` directory content:
```
+-- 2020-2-level-ctlr
    +-- tmp
        +-- articles
            +-- 1_processed.txt
            +-- 1_raw.txt
            +-- 1_meta.json
            +-- ...
```

> NOTE: When using CI (Continuous Integration), generated `dataset.zip` is available in
> build artifacts. Instructions on obtaining build artifacts *TBD*.
