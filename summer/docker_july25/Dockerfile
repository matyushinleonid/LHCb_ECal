##
## hepsw/cvmfs-lhcb
## A container where CernVM-FS is up and running
##

FROM qwaiqir/calosim:0.6.0 as builder
#WORKDIR /home/nb_user/
#COPY /home/nb_Gauss .

FROM hepsw/cvmfs-base-cc7

USER root
ENV USER root
ENV HOME /root
ENV VO_LHCB_SW_DIR /cvmfs/lhcb.cern.ch
ENV MYSITEROOT     /cvmfs/lhcb.cern.ch/lib

## make sure FUSE can be enabled
RUN if [[ ! -e /dev/fuse ]]; then mknod -m 666 /dev/fuse c 10 229; fi

WORKDIR /root

RUN mkdir -p /cvmfs/lhcb.cern.ch && \
    echo "lhcb.cern.ch /cvmfs/lhcb.cern.ch cvmfs defaults 0 0" >> /etc/fstab

ADD etc-cvmfs-lhcb-local    /etc/cvmfs/config.d/lhcb.cern.ch.local
#ADD dot-bashrc              $HOME/.bashrc

RUN yum -y install \
        # Gauss (GiGaVisUI) dependencies:
        mesa-libGLU-devel \
        motif \
        motif-devel \
    && \
        yum clean all && \
        rm -rf /var/lib/apt/lists/* && \
        rm -rf /var/cache/yum

ENV NB_USER nb_user
ENV NB_UID 1000
ENV HOME /home/${NB_USER}

RUN useradd -ms /bin/bash \
        -u ${NB_UID} \
        ${NB_USER}

COPY --from=builder /home/nb_user/Gauss $HOME/Gauss/
RUN chown -R ${NB_UID} ${HOME}
RUN mkdir /home/${NB_USER}/cmtuser

WORKDIR ${HOME}

ADD . ${HOME}
USER root
RUN chmod +x run.sh

ENV LOGS_DIR=/home/nb_user/logs
RUN mkdir /home/nb_user/logs

## make the whole container seamlessly executable
ENTRYPOINT ["/usr/bin/cubied"]
CMD ["/home/nb_user/run.sh"]

## EOF
