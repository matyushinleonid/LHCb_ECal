FROM  qwaiqir/calosim_build:0.2_python36
USER nb_user
WORKDIR /home/nb_user
RUN pip3 install --user uproot
COPY --chown=nb_user:nb_user change_tcl.py change_tcl.py
COPY --chown=nb_user:nb_user get_std.py ./Gauss/Sim/LbDelphes/options
COPY --chown=nb_user:nb_user script.sh script.sh
RUN chmod +x script.sh
USER root
ENTRYPOINT ["./script.sh"]
