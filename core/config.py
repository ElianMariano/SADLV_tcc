def read_config(file='CONFIG'):
    with open(file, 'r') as f:
        lines = f.readlines()

        EPOCHS = int(lines[0][lines[0].find('=')+1:len(lines[0])-1])
        BATCH_SIZE = int(lines[1][lines[1].find('=')+1:len(lines[1])-1])
        TRAINING_FILES = lines[2][lines[2].find('=')+1:len(lines[2])].split(',')

        f.close()
        
        return (EPOCHS, BATCH_SIZE, TRAINING_FILES)