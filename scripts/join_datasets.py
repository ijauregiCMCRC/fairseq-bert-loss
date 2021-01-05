# Data
dataset = 'de-en_IWSLT2014/data'
type = 'test'
year_1 = 'tst2010'
year_2 = 'tst2011'
year_3 = 'tst2012'
year_4 = 'dev2010'
year_5 = 'dev2012'
src = 'de'
tgt = 'en'

src_1 = open('../datasets/' + dataset + '/' + type + '/' + year_1 + '.' + src)
src_1_list = []
for line in src_1:
    src_1_list.append(line)
src_2 = open('../datasets/' + dataset + '/' + type + '/' + year_2 + '.' + src)
src_2_list = []
for line in src_2:
    src_2_list.append(line)
src_3 = open('../datasets/' + dataset + '/' + type + '/' + year_3 + '.' + src)
src_3_list = []
for line in src_3:
    src_3_list.append(line)
src_4 = open('../datasets/' + dataset + '/' + type + '/' + year_4 + '.' + src)
src_4_list = []
for line in src_4:
    src_4_list.append(line)
src_5 = open('../datasets/' + dataset + '/' + type + '/' + year_5 + '.' + src)
src_5_list = []
for line in src_5:
    src_5_list.append(line)

tgt_1 = open('../datasets/' + dataset + '/' + type + '/' + year_1 + '.' + tgt)
tgt_1_list = []
for line in tgt_1:
    tgt_1_list.append(line)
tgt_2 = open('../datasets/' + dataset + '/' + type + '/' + year_2 + '.' + tgt)
tgt_2_list = []
for line in tgt_2:
    tgt_2_list.append(line)
tgt_3 = open('../datasets/' + dataset + '/' + type + '/' + year_3 + '.' + tgt)
tgt_3_list = []
for line in tgt_3:
    tgt_3_list.append(line)
tgt_4 = open('../datasets/' + dataset + '/' + type + '/' + year_4 + '.' + tgt)
tgt_4_list = []
for line in tgt_4:
    tgt_4_list.append(line)
tgt_5 = open('../datasets/' + dataset + '/' + type + '/' + year_5 + '.' + tgt)
tgt_5_list = []
for line in tgt_5:
    tgt_5_list.append(line)

joined_src = src_1_list + src_2_list + src_3_list + src_4_list + src_5_list
joined_tgt = tgt_1_list + tgt_2_list + tgt_3_list + tgt_4_list + tgt_5_list

print(len(joined_src))
print(len(joined_tgt))
assert len(joined_src) == len(joined_tgt), "Different number of sentences!"

joined_src_write = open('../datasets/' + dataset + '/' + type + '/edunov_test.' + src, 'w')
joined_tgt_write = open('../datasets/' + dataset + '/' + type + '/edunov_test.' + tgt, 'w')

for i in range(len(joined_src)):
    joined_src_write.write(joined_src[i])
    joined_tgt_write.write(joined_tgt[i])

joined_src_write.close()
joined_tgt_write.close()
