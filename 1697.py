import collections

class Pathfinder:
    def __init__( self, board={}, limit=collections.Iterable ):
        self.board = board
        self.limit = limit

        self.blacklist = []
        self.ways = []

    def add_black( self, black ):
        self.blacklist.append( black )

    def add_blacklist( self, blacklist ):
        self.blacklist.extend( blacklist )

    def add_way( self, way ):
        if not callable( way ):
            raise TypeError( "Not a function." )
        self.ways.append( way )

    def candidates( self, stt ):
        if not self.in_limit( stt ):
            raise ValueError( "Values must be in the interval" )
        cddset = set()
        for way in self.ways:
            if self.is_placeable( way( stt ) ):
                cddset.add( way( stt ) )
        return cddset

    def explore( self, stt, end ):
        if not (self.in_limit( stt ) and self.in_limit( end )):
            raise ValueError( "Values must be in the interval" )
        bfsq = collections.deque()
        bfsq.append( [stt] )
        visited = [False for x in range( 100001 )]
        minpath = None
        while bfsq:
            curpath = bfsq.popleft()
            cur = curpath[-1]
            if minpath is not None and len( curpath ) >= len( minpath ):
                continue
            if cur is end:
                minpath = curpath
                continue
            cddset = self.candidates( cur )
            for cdd in cddset:
                if not visited[cdd]:
                    cddpath = curpath + [cdd]
                    visited[cdd] = True
                    bfsq.append( cddpath )
        return minpath
    
    def in_blacklist( self, stt ):
        brd = self.board
        if stt in brd.keys() and brd[stt] in self.blacklist:
            return True
        return False

    def in_limit( self, stt ):
        lim = self.limit
        lb, ub = 0, 0
        if isinstance( stt, collections.Iterable ):
            for idx, num in enumerate( stt ):
                lb, ub = min( lim[0][idx], lim[1][idx] ), max( lim[0][idx], lim[1][idx] )
                if not (num >= lb and num <= ub):
                    return False
        else:
            lb, ub = min( lim ), max( lim )
            if not (stt >= lb and stt <= ub):
                return False
        return True

    def is_placeable( self, stt ):
        return self.in_limit( stt ) and not self.in_blacklist( stt )

if __name__ == '__main__':
    N, K = [int( x ) for x in input().split()]
    if N >= K:
        print( N-K )
    else:
        finder = Pathfinder( limit=(0, 100000) )
        finder.add_way( lambda x: x+1 )
        finder.add_way( lambda x: x-1 )
        finder.add_way( lambda x: x*2 )
        path = finder.explore( N, K )
        print( len( path ) - 1 )
