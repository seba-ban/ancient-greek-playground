FROM python:3.11 as downloader

WORKDIR /downloads
# TODO: check checksum
RUN wget https://exist-db.org/exist/apps/public-repo/public/shared-resources-0.9.1.xar


FROM existdb/existdb:debug

# getting such an error:
# 26 Nov 2023 12:57:41,948 [main] INFO  (Deployment.java [installAndDeploy]:264) - Installing package file:///exist/autodeploy/canonical-greekLit-0.1.xar 
# 26 Nov 2023 12:57:43,369 [main] INFO  (Deployment.java [installAndDeploy]:277) - Deploying package https://github.com/PerseusDL/canonical-greekLit 
# 26 Nov 2023 12:57:45,449 [main] WARN  (StartupTriggersManager.java [startPreMultiUserSystem]:64) - StartupTrigger threw RuntimeException: Document contains at least one immense term in field="136000d0000" (whose UTF8 encoding is longer than the max length 32766), all of which were skipped.  Please correct the analyzer to not produce such terms.  The prefix of the first immense term is: '[10, -49, -128, -49, -127, -31, -65, -74, -49, -124, -50, -65, -50, -67, 32, -31, -68, -108, -49, -121, -50, -75, -50, -71, 32, -50, -102, -49, -127, -50]...', original message: bytes can be at most 32766 in length; got 45357. IGNORING! 
# java.lang.IllegalArgumentException: Document contains at least one immense term in field="136000d0000" (whose UTF8 encoding is longer than the max length 32766), all of which were skipped.  Please correct the analyzer to not produce such terms.  The prefix of the first immense term is: '[10, -49, -128, -49, -127, -31, -65, -74, -49, -124, -50, -65, -50, -67, 32, -31, -68, -108, -49, -121, -50, -75, -50, -71, 32, -50, -102, -49, -127, -50]...', original message: bytes can be at most 32766 in length; got 45357

# RUN sed -i 's,<module id="lucene-index" buffer="32" class="org.exist.indexing.lucene.LuceneIndex" />,<module id="lucene-index" buffer="48" class="org.exist.indexing.lucene.LuceneIndex" />,' /exist/etc/conf.xml
# the above doesn't solve the problem
# not sure what to do, is it even worth it?

COPY *.xar /exist/autodeploy
COPY --from=downloader /downloads/*.xar /exist/autodeploy