```python2 projectArguments.py train_full.dat test_full.dat dev_full.dat essays.aligned essays.aligned.bidirectional```

   * ``essays.aligned`` gives aligned sentences in English and German
   * ``essays.aligned.bidirectional`` provides the word alignment information on the sentences from ``essays.aligned``. These are generated (e.g.) by fast_align
   * ``train/dev/test_full.dat`` holds the argument annotated data in English
   * **Output**: the projected argumentation span annotation on the German data
