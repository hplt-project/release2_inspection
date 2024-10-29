# Nikolay, [rus_Cyrl/batch0.tsv](../annot_round1/rus_Cyrl/batch0.tsv)
Almost all examples are in the correct language, 1 example is the first part in Russian and the second in Ukrainian. 

Lots of commercial ads, some contain more running texts (e.g. descriptions of hotels), some less (e.g. sound equipment).

Occasionally the first part contains traces of menus, while the second part consists of running text.

# Marta,  [spa_Latn/batch0.tsv](../annot_round1/spa_Latn/batch0.tsv)
Porn:
* Mostly porn-free, only a couple of porny texts ("narrative/descriptive" porn, not just lists of porn hashtags)

Unnatural language:
* Alghough I didn't mark it as unnatural, I noticed many texts that are "cut", this is, ok text starts, then is cut with "read more", more unrelated ok texts follows, ends with "read more", etc. I think those are lists of headlines or blog posts titles.
* Some menus or breadcrumb menus.

Identified language: 
* All the samples are in the correct language (Spanish)

Other:
* In general, the content is varied (some advertising, some newspaper text, some forum threads, ...)
* Some glued words here and there. 
* Some "mixed content", this is, actual text with pieces of boilerplate inserted (i.e. 578d4b4056ba8794ede85d07dc1b1d7d or 3ff3eb1a9f4edefa9c649e928ee2671f)
* More PII than I expected, mainly phone numbers and email adresses.


# Marta,  [ast_Latn/batch0.tsv](../annot_round1/ast_Latn/batch0.tsv)
Porn: 
* No porn at all.

Unnatural language:
* A lot of Wikipedia boilerplate. I didn't mark as unnatural when only one or two "edit source" are in the text, but I marked texts as unnatural when too many "edit source" are present.

Identified language:
* Only about half of the examples are in the correct language (Asturian). The rest are either in Spanish, or other Spanish minority languages (Extremeño, Aragonese, ...) that are quite similar to Asturian.
* A lot of random list of contents for SEO (i.e. songs names) that are not even in Asturian.

Other:
* Batch is mostly Wikipedia. Maybe we want to enhance the wikipedia boilerplate removal (see "unnatural language" above).
* All the non-Asturian documents came from Wikipedia (either ext, Extremeño, or an, Aragonese). These could be easily filtered out if we discard Wikipedia documents from  other languages that are not the target language (ast, Asturian, in this case).
