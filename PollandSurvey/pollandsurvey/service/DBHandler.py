import sys, string, time, logging
import transaction
from pollandsurvey.model import DBSession, metadata
from pollandsurvey import model
class DBHandler(logging.Handler):
    def __init__(self, dbSession,ipserver,user):
        logging.Handler.__init__(self)
        
        ##import mx.ODBC.Windows
        
        ##self.dsn = dsn
        ##self.uid = uid
        ##self.pwd = pwd
        self.conn =  dbSession;#mx.ODBC.Windows.connect(self.dsn, self.uid, self.pwd)
        
        
        
        self.SQL = """INSERT INTO sur_log_survey (
                        Created,
                        RelativeCreated,
                        Name,
                        LogLevel,
                        LevelText,
                        Message,
                        Filename,
                        Pathname,
                        Lineno,
                        Milliseconds,
                        Exception,
                        Thread
                   )
                   VALUES (
                        %(dbtime)s,
                        %(relativeCreated)d,
                        '%(name)s',
                        %(levelno)d,
                        '%(levelname)s',
                        '%(message)s',
                        '%(filename)s',
                        '%(pathname)s',
                        %(lineno)d,
                        %(msecs)d,
                        '%(exc_text)s',
                        '%(thread)s'
                   )""";
        
        self.SQL = """ INSERT INTO sur_log_survey(
                    ip_server,
                    relative_created,
                    name,
                    log_level,
                    level_text,
                    message,
                    file_name,
                    path_name,
                    line_no,
                    milliseconds,
                    exception,
                    thread,
                    user_name,
                    current_page
        ) VALUES(
                    '""" + ipserver + """',
                    %(relativeCreated)d,
                    '%(name)s',
                    %(levelno)d,
                    '%(levelname)s',
                    '%(message)s',
                    '%(filename)s',
                    '%(pathname)s',
                    %(lineno)d,
                    %(msecs)d,
                    '%(exc_text)s',
                    '%(thread)s',
                    '""" + user + """',''); """;
                
        
        
        
                   
        #self.cursor = self.conn.cursor()

    def formatDBTime(self, record):
        record.dbtime = time.strftime("#%m/%d/%Y#", time.localtime(record.created))

    def emit(self, record):
        try:
            #use default formatting
            self.format(record)
            #now set the database time up
            self.formatDBTime(record)
            if record.exc_info:
                record.exc_text = logging._defaultFormatter.formatException(record.exc_info)
            else:
                record.exc_text = ""
            sql = self.SQL % record.__dict__
            #print sql;
            
            conn = model.DBSession.connection();
            urser = conn.execute("SELECT * FROM tg_user;");
            print "value : " + str(urser);
            model.LogSurvey.insertSQL(sql);
            #result = model.DBSession.execute(sql);
            #model.DBSession.flush() ;
            
                
            #print result.is_insert;
            #self.cursor.execute(sql)
             
        except:
            import traceback
            ei = sys.exc_info()
            traceback.print_exception(ei[0], ei[1], ei[2], None, sys.stderr)
            del ei

    def close(self):
        #self.cursor.close()
        #self.conn.close()
        logging.Handler.close(self)
        
