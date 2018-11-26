--- data <br>
&nbsp;&nbsp;&nbsp;&nbsp; ---- files <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----- train.csv <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----- test.csv<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----- valid.csv<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----- articles.csv<br>
&nbsp;&nbsp;&nbsp;&nbsp; ---- r_files<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----- books_reps<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ---- BOOKS_REP_377.npy<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----- AGE.npy<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----- INFO.npy<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----- RATE.npy<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----- AGE_BOOKS.npy<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----- idx_to_class.npy<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ----- idx_to_title.npy<br>
--- src
--- crawlers : Has files used for crawlering websites<br>
--- models   : weights of the MLP<br>
--- data_split.py   : splitting the WeeBit corpus into train,valid,test datasets<br>
--- data_prep.py    : extract features<br>
--- lexical_feat.py : extract lexical features<br>
--- MLP_exp.py		: experiments to tune the parameters<br>
--- model.py		: bulid the model with the best parameters<br>
--- build_recommend.py : do the essentials for recommendation model(like do SVD,etc)<br>
--- do_recommend.py    : run this for recommendation  <br>
--- README<br>
--- Report.pdf<br>
