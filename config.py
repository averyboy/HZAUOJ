class app_config:
    MAIL_SERVER='smtp.qq.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME='228744592@qq.com'
    MAIL_PASSWORD='iiyopczqdflpbghe'
    MAIL_DEFAULT_SENDER='averyboy@qq.com'
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:qq228744592@localhost/test'
    SQLAlCHEMY_COMMIT_TEARDOWN=True

config={
    'app':app_config
    'test':app_config
    'default':app_config
}
    


