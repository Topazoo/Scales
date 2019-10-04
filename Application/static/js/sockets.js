// WebSocket client library

angular.module('Sockets_Library', ['ngWebSocket'])
.controller('Weight_Socket', ['$scope', '$websocket', function($scope, $websocket) {
    $scope.status = 'Offline'; //TODO - Check socket for errors or watch socket?
    $scope.weight = 0;
    $scope.reference_unit = 162;

    $scope.tare = function(){
        if( $scope.socket)
            $scope.socket.send(JSON.stringify({ action: 'tare' }));
    };

    $scope.disconnect = function() {
        if( $scope.socket)
        {
            $scope.socket.send(JSON.stringify({ action: 'disconnect' }));
            $scope.socket.close(true);
        }
    };

    $scope.connect = function() {
        $scope.socket = $websocket('ws://10.0.0.166:5001');
        $scope.socket.onError(function(){
           // $scope.connect();
        });
        $scope.socket.onOpen(function(){
            $scope.socket.send(JSON.stringify({ action: 'connect' }));

            $scope.socket.onMessage(function(message) {
                if (message && message.data)
                {
                    raw = JSON.parse(message.data);
                    if (raw && raw.data)
                    {
                        $scope.status = 'Online';
                        $scope.weight = raw.data;
                    }
                }
            });
        });
        $scope.socket.onClose(function(){
            $scope.status = 'Offline';
            $scope.weight = 0;
        });
    };
}]);