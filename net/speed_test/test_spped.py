import speedtest


def speed_test_util():
    test = speedtest.Speedtest()
    config = test.get_config()
    servers = test.get_servers()
    print(config)
    print(servers)
    # test.get_best_server()
    download = float(test.download() / 1024 / 1024 / 8)
    upload = float(test.upload() / 1024 / 1024 / 8)

    print(f'当前下载速度为：{str(download)} MB/s')

    print(f'当前上传速度为：{str(upload)} MB/s')

    print('测试已完成！')


if __name__ == '__main__':
    speed_test_util()
