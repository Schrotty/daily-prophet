#!/bin/bash
cp -arv dist/storage/ storage_old/
npm run build
cp -arv storage_old/ dist/storage/
rm -r storage_old/
