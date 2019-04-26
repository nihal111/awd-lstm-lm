import os
import matplotlib as mpl
if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')

import matplotlib.pyplot as plt


def ppl_plot(train_ppl, valid_ppl, test_ppl, title):

    assert len(train_ppl) == len(valid_ppl)
    assert len(train_ppl) == len(test_ppl)

    epochs = range(1, len(train_ppl) + 1)

    fig = plt.figure()

    plt.plot(epochs, train_ppl)
    plt.plot(epochs, valid_ppl)
    plt.plot(epochs, test_ppl)

    plt.legend(['Train', 'Valid', 'Test'], loc='upper right')

    axes = plt.gca()
    axes.set_ylim([0, 3000])

    fig.suptitle(title)

    plt.xlabel('Epochs')
    plt.ylabel('Perplexity')

    fig.savefig('{}.png'.format(title))


if __name__ == '__main__':
    a = [7, 5, 4, 3.5, 3.3, 3, 2]
    b = [6, 4, 3, 2.5, 2.2, 2.1, 2]
    c = [6.5, 4.8, 3.2, 2.7, 2.4, 2.3, 2.1]

    ppl_plot(a, b, c, 'test')
