FROM qwaiqir/calosim:build_0.5.2
USER nb_user
WORKDIR /home/nb_user
COPY --chown=nb_user:nb_user script.sh script.sh
RUN chmod +x script.sh
USER root

ENV LOGS_DIR=/home/nb_user/logs
RUN mkdir /home/nb_user/logs

ENTRYPOINT ["./script.sh"]