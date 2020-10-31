from lxml import etree
import requests

# 获取一个项目的issues列表
def get_issues_list(repo_name):
    issues_list = []
    url = 'https://github.com' + repo_name + '/issues'
    # print(url)
    response = requests.get(url)
    # 获取源码
    page_source = response.text
    tree = etree.HTML(page_source)
    # 获取issues数量
    number = tree.xpath('//*[@id="js-repo-pjax-container"]/div[1]/nav/ul/li[2]/a/span[2]')
    if len(number) == 0:
        number = '0'
    else:
        number = number[0].text
    if number.isdigit():
        number = int(number)
    else:
        number = 1000
    print(number)
    # 计算分页数量，每页25个issues
    page = 0
    if number % 25 == 0:
        page = int(number / 25)
    else:
        page = int(number / 25) + 1
    for i in range(1, page + 1):
        url = 'https://github.com' + repo_name + '/issues?page=' + str(i)
        response = requests.get(url)
        # 获取源码
        page_source = response.text
        tree = etree.HTML(page_source)
        # 获取issues超链接
        arr = tree.xpath('//*[@class="d-block d-md-none position-absolute top-0 bottom-0 left-0 right-0"]/@href')
        issues_list += arr
        # /combust/mleap/issues/716
    # 返回issues数量和列表
    return number, issues_list


# 获取一个issue的内容及评论
def get_issue_content(issue_name):
    # 拼接issue地址
    url = 'https://github.com' + issue_name
    # print(url)
    response = requests.get(url)
    page_source = response.text
    tree = etree.HTML(page_source)
    # 获取issue内容
    issue_content = tree.xpath('//table//td')[0].xpath('string(.)')

    return issue_content


if __name__ == '__main__':
    # 测试
    # get_repos_list('ML pipeline')
    # get_issues('/combust/mleap')
    # get_issue_content('/combust/mleap/issues/716')
    '''
    issue="/rust-lang/rust/issues/76833"
    content=get_issue_content(issue)
    print(content)

    '''
    with open(r'result.docx', 'w+', encoding='utf-8') as f:
        #key_words = input('please input a keyword：')
        # 获取项目列表
        #repos_list = get_repos_list(key_words)
        # 格式：/combust/mleap
        repo='/microsoft/calculator'
        # 拼接项目url
        repos_url = 'https://github.com' + repo
        print(repos_url)
        f.write('\n\n')
        #f.write(repos_url)
        f.write('\n')
        # 获取项目的issues列表
        number, issues_list = get_issues_list(repo)
        f.write(str(number))
        f.write('\n')
        # 格式：/combust/mleap/issues/716
        cnt=0
        for issue in issues_list:
            # 获取issue的内容
            issue_url = 'https://github.com' + issue
            content = get_issue_content(issue)
            # content=filter_emoji(content)
            print(issue_url)
            #f.write(issue_url)
            f.write('\n')
            f.write(str(content).strip())
            f.write('\n')
            f.flush()
            # print(content)
            # print(issue)
            cnt+=1
            print(cnt)
    print('The end!')
