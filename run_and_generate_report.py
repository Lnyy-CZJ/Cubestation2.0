import pytest
import os


def run_and_generate_report():
    # 定义测试用例目录和报告输出目录
    test_case_dir1 = r'C:\Users\Admin\Desktop\cube-接口自动化\test_case\CompetManager_test.py'
    test_case_dir2 = r'C:\Users\Admin\Desktop\cube-接口自动化\test_case\CompetManager-versa_test.py'
    json_report_dir = r'C:\Users\Admin\Desktop\cube-接口自动化\report_jsondata'
    html_report_dir = r'C:\Users\Admin\Desktop\cube-接口自动化\report'

    # 运行测试用例并生成json格式的测试报告
    # 将多个测试用例目录都包含在args_list中，这样 pytest 就会运行所有这些目录下的测试用例，并生成对应的 JSON 格式的测试报告
    args_list = ['-s', '-v', test_case_dir1, test_case_dir2, '--alluredir', json_report_dir]
    pytest.main(args_list)

    # 使用allure命令生成HTML格式的测试报告
    cmd = 'allure generate {} -o {} -c'.format(json_report_dir, html_report_dir)
    os.system(cmd)


if __name__ == '__main__':
    run_and_generate_report()
