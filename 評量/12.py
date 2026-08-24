
#請使用巢狀迴圈撰寫程式，輸出下列報表（含每人總分與各科平均，平均取小數 1 位）。欄位以 \t 分隔即可。
name  = ['王小明', '李小華', '張大同', '陳美麗']
score = [[87, 64, 88], [93, 72, 86], [80, 88, 89], [79, 91, 90]]
#          國文 英文 數學
print('姓名\t國文\t英文\t數學\t總分')
print('========================================')
for i in range(len(name)):
    total = sum(score[i])
    avg = total / len(score[i])
    print(f'{name[i]}\t{score[i][0]}\t{score[i][1]}\t{score[i][2]}\t{total}')
print(f'平均\t{sum([score[i][0] for i in range(len(name))]) / len(name):.1f}\t{sum([score[i][1] for i in range(len(name))]) / len(name):.1f}\t{sum([score[i][2] for i in range(len(name))]) / len(name):.1f}')

