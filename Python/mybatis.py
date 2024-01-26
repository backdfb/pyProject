
#라이브러리 설치

pip install pyibatis
#또는
pip install mybatis_mapper2sql

# 이제부터 코드 구간

from pyibatis import Mapper
# 또는
from mybatis_mapper2sql import get_mapper, Mapper

# MyBatis 설정 파일 경로
config_file = 'mybatis_config.xml'
# SQL 매퍼 파일 경로
mapper_file = 'user_mapper.xml'

# MyBatis 매퍼 가져오기
mapper = Mapper(config=config_file, mappers=[mapper_file])

# SQL 실행
result = mapper.sql_id.select_user(param1='value1', param2='value2')

# mybatis_config.xml은 MyBatis의 설정 파일 경로를 나타내며, user_mapper.xml은 SQL 매퍼 파일 경로이다.
# 어디까지나 예시이므로, 실제 사용하는 파일 경로로 수정해야 한다.
