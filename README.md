# Celery Tutorials

根據官方教學5.3.6，實作 Celery 任務佇列系統
https://docs.celeryq.dev/en/stable/

# Docker Services 角色:
beat: 啟動定時任務

worker1,2: 併發執行任務

worker3: 單一執行任務

redis: 結果存取 port:6379

rabbitmq: 任務分發 port:5672

flower: 任務監控 port:5555

prometheus: 時序監控 port:9090

grafana: 儀表監控 port:3000

# 定期任務一<distributed_add_task>
### (非優先級任務，並對結果進行二次運算)
<長時間加法任務>

由beat啟動大量執行任務=>rabbitmq=>分散到worker1,2併發執行=>redis=>
取回結果丟到callback任務=>redis=>取回結果


# 定期任務二<distributed_sub_task>
### (高優先級任務，指定單一worker負責)
<長時間減法任務>

由beat啟動任務=>rabbitmq=>指定到worker3執行=>redis=>取回結果
