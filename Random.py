import marshal,zlib,base64

exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
