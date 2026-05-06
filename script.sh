#!/bin/bash

set -e

VERSIONS=("20.04" "22.04" "24.04")

mkdir -p dist

for VERSION in "${VERSIONS[@]}"; do
    echo "======================================"
    echo "Gerando .deb para Ubuntu $VERSION"
    echo "======================================"

    IMAGE_NAME="rackctl-builder-ubuntu-$VERSION"

    docker build \
        --build-arg UBUNTU_VERSION="$VERSION" \
        -t "$IMAGE_NAME" \
        -f Dockerfile.build .

    CONTAINER_ID=$(docker create "$IMAGE_NAME")

    mkdir -p "dist/ubuntu-$VERSION"

    docker cp \
        "$CONTAINER_ID:/app/deb_dist/." \
        "dist/ubuntu-$VERSION/" || true

    docker rm "$CONTAINER_ID"

    # opcional limpar imagem
    docker rmi "$IMAGE_NAME" || true

    echo
    echo "Pacote gerado em dist/ubuntu-$VERSION"
    echo
done

echo "======================================"
echo "Build finalizado!"
echo "======================================"