# Data
dataset = 'de-en_TEDtalks'
type = 'dev'
year_1 = 'tst2012'
year_2 = 'tst2013'
src = 'en'
tgt = 'de'

src_1 = open('../datasets/' + dataset + '/' + type + '/' + year_1 + '.' + src)
src_1_list = []
for line in src_1:
    src_1_list.append(line)
src_2 = open('../datasets/' + dataset + '/' + type + '/' + year_2 + '.' + src)
src_2_list = []
for line in src_2:
    src_2_list.append(line)

tgt_1 = open('../datasets/' + dataset + '/' + type + '/' + year_1 + '.' + tgt)
tgt_1_list = []
for line in tgt_1:
    tgt_1_list.append(line)
tgt_2 = open('../datasets/' + dataset + '/' + type + '/' + year_2 + '.' + tgt)
tgt_2_list = []
for line in tgt_2:
    tgt_2_list.append(line)

joined_src = src_1_list + src_2_list
joined_tgt = tgt_1_list + tgt_2_list

print(len(joined_src))
print(len(joined_tgt))
assert len(joined_src) == len(joined_tgt), "Different number of sentences!"

joined_src_write = open('../datasets/' + dataset + '/' + type + '/' + year_1 + '_' + year_2 + '.' + src, 'w')
joined_tgt_write = open('../datasets/' + dataset + '/' + type + '/' + year_1 + '_' + year_2 + '.' + tgt, 'w')

for i in range(len(joined_src)):
    joined_src_write.write(joined_src[i] + '\n')
    joined_tgt_write.write(joined_tgt[i] + '\n')

joined_src_write.close()
joined_tgt_write.close()
