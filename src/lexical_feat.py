import math
import nltk

UR = 0.0001

def lex_den_feat(lexi_count,word_token):
    return  round(float(lexi_count)/word_token,3)

def ttr_feat(word_type,word_token):
    return round(float(word_type)/word_token,3)

def corr_ttr_feat(word_type,word_token):
    return round(float(word_type)/math.sqrt(2*word_token),3)

def root_ttr_feat(word_type,word_token):
    return round(float(word_type)/math.sqrt(word_token),3)

def bilog_ttr_feat(word_type,word_token):
    return round(float(math.log(word_type))/math.log(word_token),3)

def uber_ind(word_type,word_token):
    if word_type == word_token:
        return round(float(math.log(word_type)**2)/UR,3) 
    return round(float(math.log(word_type)**2)/math.log(float(word_token)/word_type),3)

def lexi_var_feat(lexi_type,lexi_count):
    return round(float(lexi_type)/lexi_count,3)

def verb_var1_feat(verb_type,verb_count):
    if verb_count == 0:
        return 0        
    return round(float(verb_type)/verb_count,3)

def sqrd_verb_var1_feat(verb_type,verb_count):
    if verb_count == 0:
        return 0        
    return round(float(verb_type**2)/verb_count,3)

def corr_verb_var1_feat(verb_type,verb_count):
    if verb_count == 0:
        return 0        
    return round(float(verb_type)/math.sqrt(2*verb_count),3)

def verb_var2_feat(verb_count,lexi_count):
    if verb_count == 0:
        return 0        
    return round(float(verb_count)/lexi_count,3)

def noun_var_feat(noun_count,lexi_count):
    return round(float(noun_count)/lexi_count,3)

def adj_var_feat(adj_count,lexi_count):
    return round(float(adj_count)/lexi_count,3)

def adv_var_feat(adv_count,lexi_count):
    return round(float(adv_count)/lexi_count,3)


def get_lexical_feat(words):
    word_dict = dict(nltk.pos_tag(words))

    noun_count=0
    verb_count=0
    adj_count =0
    adv_count =0
    lexi_count=0
    verb_list=[]
    lexi_list=[]

    word_token = len(words)
    word_type  = len(set(words))

    ttr = ttr_feat(word_type,word_token)
    root_ttr = root_ttr_feat(word_type,word_token)
    corr_ttr = corr_ttr_feat(word_type,word_token)
    bilog_ttr = bilog_ttr_feat(word_type,word_token)
    uber = uber_ind(word_type,word_token)

    for word in words:
        if 'NN' in word_dict[word]:
            noun_count+=1
            lexi_count+=1
            lexi_list.append(word)
        elif 'VB' in word_dict[word] :
            verb_count+=1
            lexi_count+=1
            verb_list.append(word)
            lexi_list.append(word)
        elif 'JJ' in word_dict[word]:
            adj_count+=1
            lexi_count+=1
            lexi_list.append(word)
        elif 'RB' in word_dict[word]:
            adv_count+=1
            lexi_count+=1
            lexi_list.append(word)

    lex_den = lex_den_feat(lexi_count,word_token)
    verb_var2 = verb_var2_feat(verb_count,lexi_count)
    noun_var  = noun_var_feat(noun_count,lexi_count)
    adj_var   = adj_var_feat(adj_count,lexi_count)
    adv_var   = adv_var_feat(adv_count,lexi_count)

    verb_type = len(set(verb_list))
    lexi_type = len(set(lexi_list))

    lexi_var  = lexi_var_feat(lexi_type,lexi_count)
    verb_var1 = verb_var1_feat(verb_type,verb_count)
    sqrd_verb_var1 = sqrd_verb_var1_feat(verb_type,verb_count)
    corr_verb_var1 = corr_verb_var1_feat(verb_type,verb_count)

    return [ttr,root_ttr,corr_ttr,bilog_ttr,uber,lex_den,verb_var2,noun_var,adv_var,adv_var,lexi_var,verb_var1,sqrd_verb_var1,corr_verb_var1]

