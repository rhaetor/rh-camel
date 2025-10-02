#!/usr/bin/env bash

# Script to find broken symlinks in the docs repo
# Creates a file "borked_symlinks.sh
# that can be edited and run to fix the symlinks
# Or else as a guide to manual corrections

OUTPUT="borked_symlinks.sh"

echo -e "#!/usr/bin/env bash\n" > "${OUTPUT}"
chmod +x "${OUTPUT}"
for F in $(find . -type l)
do
  if [[ ! -e "$F" ]]; then
   echo "ln -s -f" $(readlink "$F") "$F" >>  "${OUTPUT}"
  fi
done