FROM python:3
USER root

COPY dashboard-combustiveis/ /opt/dashboard

RUN rm /opt/dashboard/dashboard.dockerfile
RUN  pip install -r /opt/dashboard/requirements.txt

# Expose the ports we're interested in
EXPOSE 8050:8050
WORKDIR /opt/dashboard/

CMD ["python3", "index.py"]
