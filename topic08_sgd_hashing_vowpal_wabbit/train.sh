#!/bin/bash
PREC=28
SEED=17
PATH_TO_DATA='../../data/stackoverflow'

for PASS in 1 3 5; do
    for NGRAM in 1 2 3;do
        vw -d $PATH_TO_DATA/stackoverflow_train.vw --oaa 10 --loss_function hinge --random_seed $SEED -b $PREC --ngram "$NGRAM" --passes "$PASS" -f $PATH_TO_DATA/stackoverflow_model_"$PASS$NGRAM".vw --quiet --cache_file $PATH_TO_DATA/stackoverflow_train.cache
	vw -i $PATH_TO_DATA/stackoverflow_model_"$PASS$NGRAM".vw -t -d $PATH_TO_DATA/stackoverflow_valid.vw -p $PATH_TO_DATA/stackoverflow_valid_pred_"$PASS$NGRAM".txt --quiet
    done
done
