#!/bin/bash

# Import utils.
source $PYESSV_WRITER_HOME/utils.sh

# Main entry point.
main()
{
	pushd $PYESSV_WRITER_HOME || exit
	pipenv run python $PYESSV_WRITER_HOME/esgf/map.py --source=$1
	popd || exit

	log "ESGF config vocabs written to "$HOME/.esdoc/pyessv-archive
}

# Invoke entry point.
main $1
