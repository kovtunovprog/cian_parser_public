from pyvirtualdisplay import Display


def main():
    import loader
    from utils.default import parsing_process
    display = Display(visible=0, size=(1200, 800))
    display.start()

    parsing_process()


if __name__ == '__main__':
    main()
