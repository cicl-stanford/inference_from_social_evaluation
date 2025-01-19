for f in *.pdf; do sips -s format png $f --out $f.png; done
